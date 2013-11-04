#!/usr/bin/env python
import os, sys
from  jinja2 import Environment, FileSystemLoader
import yaml

cwd = os.getcwd()
jobs_data_filename = os.path.join(cwd, 'data/jobs.yaml')
outfile_name = 'resume/index.html'
with open(jobs_data_filename, 'r') as jobsfile:
    jobs = yaml.load(jobsfile.read())

env = Environment(loader=FileSystemLoader(os.path.join(cwd,'templates/')))
template = env.get_template("resume.html")

output = template.render(jobs=jobs).encode('utf8')
with open(outfile_name, 'w') as testfile:
    testfile.write(output)
print "Wrote to %s" % outfile_name
