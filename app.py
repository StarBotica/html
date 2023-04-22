import streamlit as st

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

st.markdown(html_string, unsafe_allow_html=True)
