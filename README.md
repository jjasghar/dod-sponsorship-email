# dod-cfp-sponsorship email

## Scope

This ~~app~~ script goes through our hugo instance, and finds the open CFPs and
sponsorships available, and creates an bootstrap html that we can email out to
our marketing email list.

## Usage

1. Have a `venv` python environment working
```bash
git clone git@github.com:jjasghar/dod-sponsorship-email.git
cd dod-sponsorship-email/
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```
2. Checkout the [devopsdays-web][web] repo.
```bash
git clone git@github.com:devopsdays/devopsdays-web.git
```
3. Run the main script
```bash
python main.py
```

## License & Authors

If you would like to see the detailed LICENSE click [here](./LICENSE).

- Author: JJ Asghar <awesome@ibm.com>

```text
Copyright:: 2023- IBM, Inc

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```

[web]: https://github.com/devopsdays/devopsdays-web/

