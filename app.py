import streamlit as st
import streamlit.components.v1 as components

html_string = '''
<div id="av-orbit">
    <script>
        var avOrbitProperties = {
            size: 'medium',
            lang: 'en'
        };
    </script>
    <script src="https://astroviewer.net/widgets/widgets/orbit.js"></script>
</div>
'''

components.html(html_string,height=600)
#st.markdown(html_string, unsafe_allow_html=True)
