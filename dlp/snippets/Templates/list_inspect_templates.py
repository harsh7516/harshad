# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Sample app that sets up Data Loss Prevention API inspect templates."""

import argparse


# [START dlp_list_inspect_templates]
import google.cloud.dlp


def list_inspect_templates(project: str) -> None:
    """Lists all Data Loss Prevention API inspect templates.
    Args:
        project: The Google Cloud project id to use as a parent resource.
    Returns:
        None; the response from the API is printed to the terminal.
    """

    # Instantiate a client.
    dlp = google.cloud.dlp_v2.DlpServiceClient()

    # Convert the project id into a full resource id.
    parent = f"projects/{project}"

    # Call the API.
    response = dlp.list_inspect_templates(request={"parent": parent})

    for template in response:
        print(f"Template {template.name}:")
        if template.display_name:
            print(f"  Display Name: {template.display_name}")
        print(f"  Created: {template.create_time}")
        print(f"  Updated: {template.update_time}")

        config = template.inspect_config
        print(
            "  InfoTypes: {}".format(", ".join([it.name for it in config.info_types]))
        )
        print(f"  Minimum likelihood: {config.min_likelihood}")
        print(f"  Include quotes: {config.include_quote}")
        print(
            "  Max findings per request: {}".format(
                config.limits.max_findings_per_request
            )
        )


# [END dlp_list_inspect_templates]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)

    parser.add_argument(
        "--project",
        help="The Google Cloud project id to use as a parent resource.",
    )

    args = parser.parse_args()
    list_inspect_templates(args.project)
