from pathlib import Path
import subprocess

import jinja2
from tqdm import tqdm

from config import per_school_config

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader('.'),
    trim_blocks=True,
    lstrip_blocks=True,
)
template = env.get_template('sop_master.jinja')

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
