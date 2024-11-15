import streamlit as st
from pytube import YouTube

context = {"Host":"freeyoutubedownloader-dflb5w4bmiyxxac4mespbr.streamlit.app","User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"ko,ko-KR;q=0.9,en-US;q=0.8,en;q=0.7,ja;q=0.6","Cache-Control":"no-cache","Connection":"Upgrade","Origin":"https://freeyoutubedownloader-dflb5w4bmiyxxac4mespbr.streamlit.app","Pragma":"no-cache","Sec-Websocket-Extensions":"permessage-deflate; client_max_window_bits","Sec-Websocket-Key":"i5/fqgDHCW0fLLtF1FPZ5Q==","Sec-Websocket-Protocol":"streamlit, PLACEHOLDER_AUTH_TOKEN","Sec-Websocket-Version":"13","Upgrade":"websocket","X-Forwarded-For":"192.168.0.69, 10.12.39.115","X-Streamlit-User":"eyJlbWFpbCI6IiIsImlzUHVibGljQ2xvdWRBcHAiOnRydWV9"}

def form_url_input():
    with st.form(key="url_input"):
        url = st.text_input("Youtube URL", value="https://www.youtube.com/watch?v=u81OeTGT7WA&t=454s")

        if st.form_submit_button("Submit"):
            if url:
                yt = YouTube(
                    url=url,
                    proxies={"https": "https://freeyoutubedownloader-dflb5w4bmiyxxac4mespbr.streamlit.app"},
                )
                video = yt.streams.filter(progressive=True, file_extension="mp4").first()

                st.video(video.url)

    return url


def main():
    st.title("Hello, World!")
    form_url_input()


if __name__ == "__main__":
    main()
