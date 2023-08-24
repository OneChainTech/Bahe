import streamlit as st
from PIL import Image

# 标题
st.title('巴小赫')

# 图片封面
image = Image.open('cover.png') # 请替换为实际图片路径
st.image(image, use_column_width=True)

# 上传参考音乐
# st.write('上传您喜欢的参考音乐')
# 使用Markdown和HTML实现标题居中
st.markdown("<div style='text-align: center; font-size: smaller; font-weight: 300; color: #808080;'>上传您喜欢的参考音乐</div>", unsafe_allow_html=True)

uploaded_file = st.file_uploader('', type=['mp3', 'wav'])
if uploaded_file is not None:
    st.audio(uploaded_file, format='audio/mp3')

# 音乐描述文本输入区域
st.write('描述您要生成的音乐')
music_description = st.text_area('', height=100, max_chars=None)

# 生成音乐按钮
st.write('点击生成 30s 音乐')
generate_button = st.button('生成音乐')

# 我的创作标题
st.title('我的创作')

# 用户生成音乐媒体列表
# 这里可以根据实际情况添加音乐列表
