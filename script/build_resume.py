#!/usr/bin/env python
import os, sys
from  jinja2 import Environment, FileSystemLoader
import yaml

cwd = os.getcwd()
jobs_data_filename = os.path.join(cwd, 'data/jobs.yaml')
hobbies_filename = os.path.join(cwd, 'data/hobbies.yaml')
resume_outfile_name = 'resume/index.html'
do_cv = True
if do_cv:
    cv_outfile_name = 'resume/cv.html'


with open(jobs_data_filename) as jobsfile:
    jobs = yaml.load(jobsfile.read())

with open(hobbies_filename) as hobbiesfile:
    hobbies = yaml.load(hobbiesfile.read())

env = Environment(loader=FileSystemLoader(os.path.join(cwd,'templates/')))
template = env.get_template("resume.html")

output = template.render(
            jobs=jobs,
            hobbies=hobbies,
        ).encode('utf8')

with open(resume_outfile_name, 'w') as resume_file:
    resume_file.write(output)
print "Wrote to %s" % resume_outfile_name

if do_cv:
    output = template.render(
            jobs=jobs,
            mode='cv'
        ).encode('utf8')
    with open(cv_outfile_name, 'w') as cvfile:
        cvfile.write(output)
    print "Wrote to %s" % cv_outfile_name