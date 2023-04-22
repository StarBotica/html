import streamlit as st
import streamlit.components.v1 as components

# demo para poder colocar código html en nuestra página streamlit

# código html deseado
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

# components.html proporciona una forma de crear un iframe con el html personalizado
# ideal para cuando queremos colocar un widget
components.html(html_string,height=600)
