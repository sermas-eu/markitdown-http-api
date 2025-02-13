# markitdown-http-api

An API wrapper built around markitdown

## Usage

Start the container with `docker compose up`

The endpoint `/` will return a plain text result (or an HTTP error if something goes wrong). 

To test use something as following:

```bash
curl --form file='@tests/test.pdf' http://localhost:5012/
```

It should return something like this

```
Test document PDF

Lorem ipsum dolor sit amet, consectetur adipiscing elit...
```

## Using OpenAI for OCR

Set environment variables for 

`OPENAI_API_KEY=<your key>`

Optionally set the openai model, defaults to `gpt4-o`
`OPENAI_MODEL=gpt4-o`

## License

Copyright 2025+ Spindox Labs

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
