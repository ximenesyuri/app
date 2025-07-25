from typed import null
from app.mods.types.base import Inner, Jinja
from app.mods.factories.base import Tag
from app.mods.decorators.base import component
from app.helper import (
    if_key,
    if_id,
    if_class,
    if_div,
    if_style,
    if_alpine,
    if_text,
    if_title,
    if_button,
    if_link,
    if_text,
    if_image,
    if_figure,
    if_script,
    if_asset,
    if_item,
    if_ul,
    if_ol,
    if_nav
)
from app.models import (
    Div,
    Alpine,
    Button,
    Title,
    Text,
    Image,
    Link,
    Figure,
    Script,
    Asset,
    Item,
    Ordered,
    Unordered,
    Nav
)

@component
def div(div: Div=Div(), alpine: Alpine=Alpine(), inner: Inner="") -> Jinja:
    div_data    = if_div(div)
    alpine_data = if_alpine(alpine)
    return """jinja
<div{{ div_data }}{{ alpine_data }}>{% if div.inner %}
    {{ div.inner }}
</div>{% elif inner %}
    {{ inner }}
</div>{% else %}</div>{% endif %}
"""

@component
def text(text: Text=Text(), inner: Inner="") -> Jinja:
    text_data = if_text(text)
    return """jinja
<p{{ text_data }}>{% if text.inner %}
    {{ text.inner }}
</p>{% elif inner %}
    {{ inner }}
</p>{% else %}</p>{% endif %}
"""

@component
def title(title: Title=Title(), inner: Inner="") -> Jinja:
    title_data = if_title(title)
    return """jinja
<{{ title.title_tag }}{{ title_data }}>{% if title.inner %}
    {{ title.inner }}
</{{ title.title_tag }}>{% elif inner %}
    {{ inner }}
</{{ title.title_tag }}>{% else %}</{{ title.title_tag }}>{% endif %}
"""

@component
def link(link: Link=Link(), inner: Inner="") -> Jinja:
    link_data = if_link(link)
    return """jinja
<a{{ link_data }}>{% if link.inner %}
    {{ link.inner }}
</a>{% elif inner %}
    {{ inner }}
</a>{% else %}</a>{% endif %} 
"""

@component
def image(image: Image=Image()) -> Tag('img'):
    image_data = if_link(image)
    return """jinja
<img{{ image_data }}/>
"""

@component
def figure(figure: Figure=Figure()) -> Tag('figure'):
    figure_data = if_figure(figure)
    image_data = if_image(figure.figure_img)
    return """jinja
<figure{{ figure_data }}>
    <img{{ image_data }}>
    {% if figure.figure_caption %}<figcaption>{{ figure_caption }}</figcaption>{% endif %}
</figure>
"""

@component
def button(button: Button=Button(), inner: Inner="") -> Jinja:
    button_data = if_button(button)
    return """jinja 
<button{{ button_data }}>{% if button.inner %}
    {{ button.inner }}
</button>{% elif inner %}
    {{ inner }}
</button>{% else %}</button>{% endif %}
"""

@component
def asset(asset: Asset=Asset()) -> Tag('link'):
    asset_data = if_asset(asset)
    return """jinja
<link{{ asset_data }}/>
"""

@component
def script(script: Script=Script(), inner: Inner="") -> Jinja:
    script_data = if_script(script)
    return """jinja
<script{{ script_data }}>{% if script.inner %}
    {{ script.inner }}
</script>{% elif inner %}
    {{ inner }}
</script>{% else %}</script>{% endif %}
"""

@component
def item(item: Item=Item(), inner: Inner="") -> Jinja:
    item_data = if_item(item)
    return """jinja
<li{{ item_data }}>{% if item.inner %}
    {{ item.inner }}
</li>{% elif inner %}
    {{ inner }}
</li>{% else %}</li>{% endif %}
"""
li = item

@component
def unordered(ul: Unordered=Unordered(), depends_on=[item, link]) -> Jinja:
    ul_data = if_ul(ul)
    return """jinja
<ul{{ ul_data }}>{% if ul.ul_items %}{% for i in ul.ul_items %}
    {{ item(item=i) }}{% endfor %}
</ul>{% else %}</ul>{% endif %}
"""
ul = unordered

@component
def ordered(ol: Ordered=Ordered(), depends_on=[item]) -> Jinja:
    ol_data = if_ol(ol)
    return """jinja
<ol{{ ol_data }}>{% if ol.ol_items %}{% for i in ol.ol_items %}
    {{ item(item=i) }}{% endfor %}
</ol>{% else %}</ol>{% endif %}
"""
ol = ordered


@component
def nav(nav: Nav=Nav(), depends_on=[item, link]) -> Jinja:
    nav_data = if_nav(nav)
    ul_id = if_id(nav.ul_id)
    ul_class = if_class(nav.ul_class)
    if nav.nav_direction == "horizontal":
        ul_style = f" style='display: flex; flex-direction: row; {nav.ul_style}'"
    else:
        ul_style = f" style='display: flex; flex-direction: column; {nav.ul_style}'"

    return """jinja
<nav{{nav_data}}>{% if nav.nav_items %}
    <ul{{ ul_id }}{{ ul_class }}{{ ul_style }}>{% for it in nav.nav_items %}
        {{ item(item=it, inner=link(link=it.item_link)) }}</li>{% endfor %}
    </ul>
</nav>{% else %}</nav>{% endif %}
"""
