import requests
import time
import os

FASTAPI_ENDPOINT = "http://127.0.0.1:8000/api/v1/telemetry"

def simulate_ebpf_event_stream():
    print("[Aetheris eBPF Probe] Initializing kernel tracer...")
    print("[Aetheris eBPF Probe] Monitoring syscalls (e.g. execve, openat)...")
    
    # Kernel telemetry mock loop for initial engine integration testing
    try:
        while True:
            event_payload = {
                "pid": os.getpid(),
                "process_name": "ebpf-tracer",
                "syscall": "sys_execve",
                "severity": "INFO"
            }
            try:
                res = requests.post(FASTAPI_ENDPOINT, json=event_payload, timeout=2)
                print(f"[+] Event sent to FastAPI Engine | Status: {res.status_code}")
            except Exception as e:
                print(f"[-] Failed to push event to FastAPI: {e}")
            
            time.sleep(5)
    except KeyboardInterrupt:
        print("\n[Aetheris eBPF Probe] Stopped monitoring.")

if __name__ == "__main__":
    simulate_ebpf_event_stream()
