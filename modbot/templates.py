
def render_template(template, context={}):
    with open(f"./templates/{template}") as f:
        template = f.read()
    return template.format(**context)