from agent import get_agent
import streamlit as st

st.set_page_config(
    page_title="Email Agent",
    page_icon="📧"
)

st.subheader("📧 Email Agent")
st.caption("Send professional emails with the appropriate resume automatically.")


if "messages" not in st.session_state:
    st.session_state.messages = []

if "agent" not in st.session_state:
    st.session_state.agent = get_agent()



for msg in st.session_state.messages:

    role = msg.get("role")

   
    if role == "ai":
        role = "assistant"

    st.chat_message(role).markdown(
        msg.get("content", "")
    )




query = st.chat_input("Ask anything...")


if query:

    
    st.session_state.messages.append({
        "role": "user",
        "content": query
    })

    st.chat_message("user").markdown(query)

    try:

        # Invoke LangGraph agent
        res = st.session_state.agent.invoke(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": query
                    }
                ]
            },
            {
                "configurable": {
                    "thread_id": "chat_1"
                }
            }
        )

        # Get latest assistant response
        ans = res["messages"][-1].content

        # Save response
        st.session_state.messages.append({
            "role": "ai",
            "content": ans
        })

        # Display response
        st.chat_message("assistant").markdown(ans)

    except Exception as e:

        st.error("Something went wrong.")

        st.exception(e)
    
    