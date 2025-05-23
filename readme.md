# OpenStack Cloud Service Orchestrator

This project delivers an automated solution designed to deploy, operate, and manage a scalable web service within an OpenStack cloud environment. It integrates various cloud technologies and automation tools to provide a resilient and self-managing service architecture.

## Overview

The solution orchestrates the lifecycle of a Flask-based web service, along with its associated SNMP daemon, across a cluster of OpenStack instances. It provides a robust framework for continuous monitoring, dynamic scaling (both up and down) based on a configurable desired node count, and complete resource cleanup. Centralized management is achieved through dedicated Bastion and Proxy nodes, ensuring secure and efficient operations.

## Prerequisites

To utilize this solution, ensure the following tools are installed and configured on your local machine:

*   **Bash Environment:** A Unix-like command-line environment.
*   **OpenStack Client (CLI):** Installed and configured to interact with your OpenStack cloud. Verify connectivity with `openstack project list`.
*   **SSH Client:** For secure shell access. Ensure your SSH agent is running if you use one.
*   **Python 3:** Required for local scripts like `alive.py` and `service.py`, though deployed by Ansible. `ping3` should be installed (e.g., `pip3 install ping3`).
*   **`curl` (Optional but Recommended):** For web service validation.
*   **`snmpwalk` (Optional but Recommended):** From `snmp` or `net-snmp-tools` package, for SNMP service validation.

## Local Machine Setup

Before running the scripts, prepare your local environment:

1.  **SSH Keypair Generation:** Generate an SSH keypair for secure access to OpenStack instances.
    ```bash
    ssh-keygen -t rsa -b 4096 -f ~/.ssh/myKey
    ```
    Replace `myKey` with your desired key name. Ensure `~/.ssh/myKey` (private key) and `~/.ssh/myKey.pub` (public key) are created.
2.  **OpenStack RC File:** Place your OpenStack `openrc.sh` (or `.rc`) file directly in the root directory of this project. This file contains your cloud credentials.
3.  **`servers.conf` Configuration:** Create a file named `servers.conf` in the project root. This file should contain a single integer on its first line, specifying the initial desired number of service nodes.
    ```bash
    echo 3 > servers.conf
    ```
    This example sets the initial desired node count to 3.
4.  **Project Structure:** Ensure all Ansible playbooks, Python scripts, and Jinja2 templates are organized within a `src/` subdirectory. The solution expects the following structure:
    ```
    .
    ├── operate
    ├── install
    ├── cleanup
    ├── my_openrc_file  (your OpenStack RC file)
    ├── servers.conf
    └── src/
        ├── site.yaml
        ├── alive.py
        ├── service.py
        ├── haproxy.cfg.j2
        ├── nginx.conf.j2
        └── nodes.txt.j2
    ```

## Scripts

All primary operations are encapsulated in three main Bash scripts, each serving a distinct operational mode: `install` for deployment, `operate` for continuous monitoring and scaling, and `cleanup` for resource tear-down.

### General Usage Pattern

All scripts are consistent command-line interface:

```bash
./<script_name> <openrc_file> <tag> <ssh_key_name>
```