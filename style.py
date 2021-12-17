import math
import pandas as pd
import requests
import streamlit as st
import time
import os

def shishikan():
        st.write(
        """<h2><img src="data:image/x-icon;base64,AAABAAEAICAAAAEAIACoEAAAFgAAACgAAAAgAAAAQAAAAAEAIAAAAAAAABAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////v7+//7+/v/+/v7////////////+/v7//Pz8//z8/P/9/f3////////////9/f3//Pz8//z8/P/9/f3////////////+/v7//v7+//7+/v//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////+fn5/+Xl5f/m5ub/5+fn//v7+///////3t7e/7e3t/+5ubn/ysrK////////////zMzM/7m5uf+3t7f/29vb///////7+/v/5+fn/+bm5v/l5eX/+fn5/////////////////////////////////////////////v7+///////t7e3/tLS0/7e3t/+6urr/9PT0//////+fn5//Kysr/zIyMv9jY2P///////////9qamr/MTEx/ywsLP+Xl5f///////X19f+6urr/t7e3/7S0tP/t7e3///////7+/v/////////////////////////////////+/v7//////+7u7v+6urr/vLy8/7+/v//19fX//////6ampv87Ozv/QkJC/29vb////////////3V1df9BQUH/PDw8/5+fn///////9fX1/7+/v/+8vLz/urq6/+7u7v///////v7+//////////////////////////////////7+/v//////7u7u/7m5uf+7u7v/vr6+//X19f//////paWl/zg4OP8/Pz//bGxs////////////c3Nz/z09Pf85OTn/nZ2d///////19fX/vr6+/7u7u/+5ubn/7u7u///////+/v7//////////////////////////////////v7+///////u7u7/ubm5/7u7u/++vr7/9fX1//////+lpaX/ODg4/z8/P/9sbGz///////////9zc3P/PT09/zk5Of+dnZ3///////X19f++vr7/u7u7/7m5uf/u7u7///////7+/v/////////////////////////////////+/v7//////+7u7v+5ubn/u7u7/76+vv/19fX//////6Wlpf84ODj/Pz8//2xsbP///////////3Nzc/89PT3/OTk5/52dnf//////9fX1/76+vv+7u7v/ubm5/+7u7v///////v7+//////////////////////////////////7+/v//////7u7u/7m5uf+7u7v/vr6+//X19f//////paWl/zg4OP8/Pz//bGxs////////////c3Nz/z09Pf85OTn/nZ2d///////19fX/vr6+/7u7u/+5ubn/7u7u///////+/v7//////////////////////////////////v7+///////u7u7/ubm5/7u7u/++vr7/9fX1//////+lpaX/ODg4/z8/P/9sbGz///////////9zc3P/PT09/zk5Of+dnZ3///////X19f++vr7/u7u7/7m5uf/u7u7///////7+/v/////////////////////////////////+/v7//////+7u7v+5ubn/u7u7/76+vv/19fX//////6Wlpf84ODj/Pz8//2xsbP///////////3Nzc/89PT3/OTk5/52dnf//////9fX1/76+vv+7u7v/ubm5/+7u7v///////v7+//////////////////////////////////7+/v//////7u7u/7m5uf+7u7v/vr6+//X19f//////paWl/zg4OP8/Pz//bGxs////////////c3Nz/z09Pf85OTn/nZ2d///////19fX/vr6+/7u7u/+5ubn/7u7u///////+/v7//////////////////////////////////v7+///////u7u7/t7e3/7m5uf+8vLz/9fX1//////+lpaX/ODg4/z8/P/9sbGz///////////9zc3P/PT09/zk5Of+dnZ3///////X19f+8vLz/ubm5/7e3t//u7u7///////7+/v/////////////////////////////////+/v7//////+/v7/+/v7//wcHB/8TExP/19fX//////6Wlpf84ODj/Pz8//2xsbP///////////3Nzc/89PT3/OTk5/52dnf//////9fX1/8TExP/BwcH/v7+//+/v7////////v7+/////////////////////////////////////////////v7+//r6+v/6+vr/+vr6//r6+v//////paWl/zg4OP8/Pz//bGxs////////////c3Nz/z09Pf85OTn/nZ2d///////6+vr/+vr6//r6+v/6+vr//v7+/////////////////////////////////////////////////////////////////////////////Pz8//////+lpaX/ODg4/z8/P/9sbGz///////////9zc3P/PT09/zk5Of+fn5////////z8/P/////////////////////////////////////////////////////////////////9/f3//////9vb2/9tbW3/dHR0/3Nzc/9ycnL/dnZ2/1xcXP9CQkL/PDw8/2xsbP///////////25ubv88PDz/Q0ND/1paWv92dnb/cnJy/3Nzc/90dHT/bW1t/9vb2////////f39//////////////////////////////////39/f//////zs7O/zU1Nf8/Pz//PT09/z09Pf88PDz/QkJC/0pKSv8+Pj7/b29v////////////bm5u/z4+Pv9KSkr/QkJC/z09Pf89PT3/PT09/z8/P/81NTX/zs7O///////9/f3//////////////////////////////////f39///////Nzc3/MTEx/zs7O/85OTn/OTk5/zk5Of84ODj/OTk5/y4uLv9iYmL///////////9iYmL/Li4u/zk5Of84ODj/OTk5/zk5Of85OTn/Ozs7/zExMf/Nzc3///////39/f/////////////////////////////////+/v7//////+bm5v+ampr/n5+f/56env+enp7/np6e/56env+fn5//mpqa/7Kysv///////////7Kysv+ampr/n5+f/56env+enp7/np6e/56env+fn5//mpqa/+bm5v///////v7+/////////////////////////////////////////////v7+/////////////////////////////////////////////////////////////////////////////////////////////////////////////v7+///////////////////////////////////////////////////////+/v7//Pz8//z8/P/8/Pz//Pz8//z8/P/8/Pz//Pz8//z8/P/9/f3////////////9/f3//Pz8//z8/P/8/Pz//Pz8//z8/P/8/Pz//Pz8//z8/P/+/v7/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=" style="font-size: 1.5em;">Tensor Data Platform</h2>
Parameters
""",
        unsafe_allow_html=True,
    )
