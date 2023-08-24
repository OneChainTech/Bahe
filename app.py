import streamlit as st
from PIL import Image
from gradio_client import Client
import tempfile

# 标题
# st.title('巴小赫')
st.markdown("<div style='text-align: left; font-size: 20px; margin-bottom: 15px;'>巴小赫</div>", unsafe_allow_html=True)

# 图片封面
image = Image.open('cover.png') # 请替换为实际图片路径
st.image(image, use_column_width=True)

# 上传参考音乐
st.write('上传您喜欢的参考音乐')
# 使用Markdown和HTML实现标题居中
# st.markdown("<div style='text-align: center; font-size: smaller; font-weight: 300; color: #808080;'>上传您喜欢的参考音乐</div>", unsafe_allow_html=True)

uploaded_file = st.file_uploader('', type=['mp3', 'wav'])
if uploaded_file is not None:
    st.audio(uploaded_file, format='audio/mp3')
    
    # 创建一个临时文件
    tfile = tempfile.NamedTemporaryFile(delete=False) 
    tfile.write(uploaded_file.read())

    # 获取临时文件的路径
    path = tfile.name

# 音乐描述文本输入区域
st.write('描述您要生成的音乐')
music_description = st.text_area('', height=100, max_chars=300)

# 生成音乐按钮
st.write('点击生成 30s 音乐')
# generate_button = st.button('生成音乐')
# 使用列来居中按钮
col1, col2, col3, col4, col5 = st.columns(5)

with col3:
    button = st.button('生成音乐')

# 存储已生成的音乐文件路径
generated_music_files = []

# 按钮点击事件
if button:
    client = Client("https://facebook-musicgen--xstnr.hf.space/")
    result = client.predict(
                    music_description,
                    path,
                    fn_index=0
    )
    # print(result)
    generated_music_files.append(result)  

    st.markdown("<div style='text-align: left; font-size: 20px; margin-bottom: 15px;'>我的创作</div>", unsafe_allow_html=True)
    for music_file in generated_music_files:
        st.audio(music_file)
