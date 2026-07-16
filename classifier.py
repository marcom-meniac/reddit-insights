"""
classifier.py

Rule-based technology classifier for Reddit Marketing Intelligence.
"""

from typing import Dict, List

RULES: Dict[str, List[str]] = {

    "Artificial Intelligence": [
        "ai","artificial intelligence","gen ai","generative ai",
        "machine learning","ml","deep learning","neural network",
        "transformer","llm","foundation model","agentic ai",
        "rag","vector database","embedding","prompt engineering",
        "fine tuning","inference","training","gpu","cuda",
        "tensorflow","pytorch","onnx","huggingface",
        "chatgpt","gpt","claude","gemini","copilot",
        "llama","mistral","falcon","deepseek","openrouter",
        "anthropic","openai","google ai","vertex ai",
        "azure openai","amazon bedrock","ollama","vllm"
    ],

    "Cloud Computing": [
        "cloud","cloud computing","iaas","paas","saas",
        "private cloud","public cloud","hybrid cloud",
        "multi cloud","cloud native",

        "aws","amazon web services",
        "azure","microsoft azure",
        "gcp","google cloud",
        "oracle cloud","oci",
        "ibm cloud",
        "alibaba cloud",
        "digitalocean",
        "linode",
        "akamai cloud",
        "vultr",
        "ovh",
        "hetzner"
    ],

    "Data Center": [
        "data center","datacenter","colo","colocation",
        "rack","server rack","blade server",
        "power","ups","generator",
        "cooling","precision cooling",
        "hvac","tier iii","tier iv",
        "dcim","facility",

        "ctrls","ctrls datacenters",
        "stt gdc","st telemedia",
        "sify","sify technologies",
        "yotta","yotta infrastructure",
        "nxtra","nxtra by airtel",
        "netmagic","ntt netmagic",
        "ntt","adani connx",
        "web werks",
        "esds",
        "e2e networks"
    ],
    "Enterprise Applications": [
        "sap",
        "sap hana",
        "sap basis",
        "oracle erp",
        "oracle fusion",
        "erp",
        "crm",
        "salesforce",
        "servicenow",
        "workday",
        "dynamics 365",
        "microsoft dynamics"
    ],

    "Virtualization": [
        "vmware","vsphere","vcenter",
        "esxi","hyper-v","kvm",
        "xen","xcp-ng","proxmox",
        "nutanix","hypervisor",
        "virtualization","virtual machine","vm"
    ],

    "Containers & Kubernetes": [
        "docker","container","containerd",
        "podman","kubernetes","k8s",
        "helm","openshift","rancher",
        "eks","aks","gke",
        "service mesh","istio",
        "kubevirt"
    ],

    "Cybersecurity": [
        "cybersecurity","security",
        "zero trust","iam","pam","mfa","sso",
        "firewall","waf","ids","ips",
        "siem","soc","xdr","edr",
        "vulnerability","cve",
        "penetration testing","pentest",
        "ransomware","malware",
        "phishing","ddos",
        "threat intelligence",
        "crowdstrike","sentinelone",
        "palo alto","fortinet",
        "checkpoint","zscaler",
        "okta","cyberark"
    ],

    "Networking": [
        "network","networking",
        "router","switch","gateway",
        "sd-wan","vpn","dns","dhcp",
        "tcp","udp","bgp","ospf",
        "load balancer","nginx","haproxy",
        "f5","cisco","juniper",
        "arista","mikrotik","ubiquiti"
    ],

    "Storage": [
        "storage","san","nas",
        "object storage","block storage",
        "ssd","nvme","hdd",
        "backup","restore","snapshot",
        "replication","deduplication",
        "netapp","pure storage",
        "dell emc","hitachi vantara",
        "ceph","minio"
    ],

    "Database": [
        "database","postgresql","postgres",
        "mysql","mariadb",
        "oracle database","sql server",
        "mongodb","redis","cassandra",
        "elasticsearch","opensearch",
        "clickhouse","snowflake"
    ],

    "DevOps": [
        "devops","devsecops",
        "ci/cd","pipeline",
        "github actions","gitlab ci",
        "jenkins","argo cd",
        "terraform","ansible","chef","puppet",
        "infrastructure as code","iac",
        "automation"
    ],

    "Observability": [
        "observability","monitoring",
        "apm","logging","metrics",
        "distributed tracing",
        "opentelemetry",
        "grafana","prometheus",
        "loki","tempo",
        "elastic","elk",
        "splunk",
        "new relic",
        "dynatrace",
        "datadog",
        "appdynamics"
    ],

    "Compliance": [
        "gdpr","hipaa",
        "iso 27001","iso27001",
        "pci dss","soc2",
        "dpdp","cert-in",
        "nist","rbi",
        "sebi","audit",
        "compliance","governance"
    ],

    "GPU & HPC": [
        "gpu","gpu cluster",
        "h100","h200",
        "a100","a30","a40",
        "rtx","tesla",
        "nvidia","amd instinct",
        "cuda","nccl",
        "high performance computing",
        "hpc","slurm"
    ],

    "Backup & Disaster Recovery": [
        "backup","restore",
        "business continuity",
        "disaster recovery","dr",
        "rpo","rto",
        "veeam",
        "commvault",
        "rubrik",
        "cohesity"
    ],

    "Edge Computing": [
        "edge computing",
        "edge ai",
        "iot",
        "industrial iot",
        "fog computing",
        "5g edge",
        "micro data center"
    ]
}


def classify(text: str) -> str:
    """
    Classify text into a high-level technology category.

    Parameters
    ----------
    text : str
        Reddit post title and/or body.

    Returns
    -------
    str
        Matching technology category or 'Other'.
    """

    if not text:
        return DEFAULT_CATEGORY

    text = text.lower().strip()

    for topic, keywords in RULES.items():
        if any(keyword in text for keyword in keywords):
            return topic

    return DEFAULT_CATEGORY