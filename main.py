import streamlit as st
from pytube import YouTube


def form_url_input():
    with st.form(key="url_input"):
        url = st.text_input("Youtube URL", value="https://www.youtube.com/watch?v=u81OeTGT7WA&t=454s")

        if st.form_submit_button("Submit"):
            if url:
                yt = YouTube(
                    url=url,
                )
                st.write(st.context.headers.to_dict())
                video = yt.streams.filter(progressive=True, file_extension="mp4").first()

                st.video(video.url)

    return url


def main():
    st.title("Hello, World!")
    form_url_input()


if __name__ == "__main__":
    main()
