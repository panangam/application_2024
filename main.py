from pathlib import Path
import subprocess
import argparse

import jinja2
from tqdm import tqdm

from config import per_school_config

parser = argparse.ArgumentParser()
parser.add_argument('prefix', nargs='?', default=None, help='Folder name, which is probably the school name. If not given, run all.')
args = parser.parse_args()

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader('.'),
    trim_blocks=True,
    lstrip_blocks=True,
)
template = env.get_template('sop_master.jinja')

if args.prefix is not None:
    per_school_config = {args.prefix: per_school_config[args.prefix]}

for prefix in (pbar := tqdm(per_school_config.keys())):
    pbar.set_description(prefix)
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
