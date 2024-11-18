default_config = dict(
    is_master=True,
    school='XXXXX NOT SET! XXXXX',
    school_paragraph='XXXXX NOT SET! XXXXX',
    include_personal_paragraph=True,
    header_extra='',
)

def read_text(file):
    with open(file) as fin:
        return fin.read()

_override_configs = dict(
    cmu=dict(
        school='CMU',
    ),
    usc=dict(
        school='USC',
    ),
    ucsd=dict(
        school='UCSD',
    )
)

prefixes = list(_override_configs.keys())

# add school paragraphs
for prefix in prefixes:
    _override_configs[prefix]['school_paragraph'] = read_text(f"{prefix}/{prefix}_paragraph.md")

# expand to full config
per_school_config = dict()
for prefix in prefixes:
    per_school_config[prefix] = {
        **default_config,
        **_override_configs[prefix],
    }
