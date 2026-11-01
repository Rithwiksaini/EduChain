"""VidyaRL master Streamlit application entrypoint."""
from __future__ import annotations

import streamlit as st

from core_engine.rl_router import RLRouter
from database.connection import get_session, init_db
from database.crud import seed_curriculum
from views.auth_view import ensure_demo_accounts, login_view, require_role
from views.student_dashboard import render as render_student
from views.teacher_cockpit import render as render_teacher


@st.cache_resource

def bootstrap() -> bool:
    init_db()
    with get_session() as session:
        seed_curriculum(session)
        ensure_demo_accounts(session)
    RLRouter().save()
    return True


def initialize_session() -> None:
    st.session_state.setdefault("auth", None)
    st.session_state.setdefault("teacher_overrides", {})


def main() -> None:
    st.set_page_config(page_title="VidyaRL — Learning GPS", page_icon="📚", layout="centered", initial_sidebar_state="expanded")
    bootstrap()
    initialize_session()

    if not st.session_state.get("auth"):
        with get_session() as session:
            login_view(session)
        return

    auth = st.session_state["auth"]
    with st.sidebar:
        st.markdown(f"### 📚 VidyaRL\n**{auth['display_name']}**")
        page = st.radio("Navigate", ["Student Dashboard", "Teacher Cockpit"] if auth["role"] == "teacher" else ["Student Dashboard"])
        if st.button("Sign out", use_container_width=True):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()

    with get_session() as session:
        if page == "Teacher Cockpit" and require_role("teacher"):
            render_teacher(session)
        elif page == "Student Dashboard":
            render_student(session)
        else:
            st.error("You are not authorized for this view.")


if __name__ == "__main__":
    main()
