from pathlib import Path
import subprocess

import jinja2
from tqdm import tqdm

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader('.'),
    trim_blocks=True,
    lstrip_blocks=True,
)
template = env.get_template('sop_master.jinja')

default_config = dict(
    is_master=True,
    school='XXXXX NOT SET! XXXXX',
    school_paragraph='XXXXX NOT SET! XXXXX',
    include_personal_paragraph=True,
    header_extra='',
)

with open('cmu/cmu_paragraph.md') as fin:
    cmu_paragraph = fin.read().strip()
cmu_config = {
    **default_config,
    **dict(
        school='CMU',
        is_master=True,
        school_paragraph=cmu_paragraph,
        header_extra=', CMU Application ID panangam@gmail.com'
    ),
}
with open('usc/usc_paragraph.md') as fin:
    usc_paragraph = fin.read().strip()
usc_config = {
    **default_config,
    **dict(
        school='USC',
        is_master=True,
        school_paragraph=usc_paragraph
    )
}
with open('ucsd/ucsd_paragraph.md') as fin:
    ucsd_paragraph = fin.read().strip()
ucsd_config = {
    **default_config,
    **dict(
        school='UCSD',
        is_master=True,
        school_paragraph=ucsd_paragraph
    )
}

per_school_config = dict(
    usc=usc_config,
    cmu=cmu_config,
    ucsd=ucsd_config,
)

for prefix in tqdm(per_school_config.keys()):
    config = per_school_config[prefix]

    sop_text = template.render(config)

    with open(f'{prefix}/{prefix}_sop.md', 'w') as fout:
        fout.write(sop_text)

    subprocess.run([
        'pandoc', 
        f'{prefix}/{prefix}_sop.md', 
        '-o', f'{prefix}/{prefix}_sop_oras_phongpanangam.pdf',
        # '--template', './default_modded.latex'
        # '-t', 'html'
    ])
