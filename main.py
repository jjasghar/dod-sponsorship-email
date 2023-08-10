#!/usr/bin/env python

import os
import re
import yaml
from datetime import datetime
from jinja2 import Environment, FileSystemLoader, PackageLoader


def render_email(data_file, j2template, output_file):
    with open(data_file, 'r') as file:
        try:
            data = file.read()
        except Exception as err:
            print(err)

    env = Environment(
        loader=FileSystemLoader(searchpath="."),
        trim_blocks=True,
        lstrip_blocks=True
    )

    template = env.get_template(name=j2template)
    rendered = template.render(data)
    with open(output_file, "w") as file:
        file.write(rendered)


output_date = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
print(output_date)


files = [f for f in os.listdir('devopsdays-web/data/events') if
         re.match('202[3-4]+.*\.yml', f)]

print("*********")
print("---- Getting open CFP -----")
print("*********")

with open("email.yml", "w") as f:
    f.write("---\n")
    f.write("cfp:\n")

counter = 1
for file in files:
    with open(f'devopsdays-web/data/events/{file}', "r") as stream:
        try:

            yaml_file = yaml.safe_load(stream)
            try:
                if yaml_file['cfp_open'] != "false" or "no":
                    try:
                        date_object = datetime.strptime(str(yaml_file['enddate']), '%Y-%m-%d %H:%M:%S%z')
                        if date_object.date() < datetime.today().date():
                            continue
                        else:
                            with open("email.yml", "a") as f:
                                f.write(f"  - name: {yaml_file['name']}\n")
                                f.write(f"    count: {counter}\n")
                                f.write(f"    main_link: https://devopsdays.org/events/{yaml_file['name']}/welcome/\n")
                                f.write(f"    cfp_link: {yaml_file['cfp_link']}\n")
                                f.write(f"    reg_link: {yaml_file['registration_link']}\n")
                                counter += 1
                    except:
                        continue

            except KeyError:
                continue

        except yaml.YAMLError as exc:
            print(exc)

print("*********")
print("---- Getting open sponsorship -----")
print("*********")

with open("email.yml", "a") as f:
    f.write("sponsorship:\n")

counter = 1
for file in files:
    with open(f'devopsdays-web/data/events/{file}', "r") as stream:
        try:

            yaml_file = yaml.safe_load(stream)

            try:
                if yaml_file['sponsors_accepted'] != "false" or "no":
                    try:
                        date_object = datetime.strptime(str(yaml_file['enddate']), '%Y-%m-%d %H:%M:%S%z')
                        if date_object.date() < datetime.today().date():
                            continue
                        else:
                            with open("email.yml","a") as f:
                                f.write(f"  - name: {yaml_file['name']}\n")
                                f.write(f"    count: {counter}\n")
                                f.write(f"    main_link: https://devopsdays.org/events/{yaml_file['name']}/welcome/\n")
                                f.write(f"    cfp_link: {yaml_file['cfp_link']}\n")
                                f.write(f"    reg_link: {yaml_file['registration_link']}\n")
                                counter += 1
                    except:
                        continue


            except KeyError:
                continue

        except yaml.YAMLError as exc:
            print(exc)

if __name__ == "__main__":
    render_email(data_file="email.yml", j2template="email.html.j2", output_file="index.html")
