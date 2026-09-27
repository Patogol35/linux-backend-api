from flask import Flask, jsonify
from flask_cors import CORS
import psutil
import platform
import time

app = Flask(__name__)
CORS(app)


# =========================
# HEALTH
# =========================

@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({
        "status": "online",
        "message": "Linux Server Monitor API funcionando"
    })


# =========================
# SYSTEM
# =========================

@app.route("/api/system", methods=["GET"])
def system_info():

    memory = psutil.virtual_memory()
    disk = psutil.disk_usage("/")

    return jsonify({
        "system": platform.system(),
        "hostname": platform.node(),
        "release": platform.release(),
        "version": platform.version(),
        "architecture": platform.machine(),

        "cpu": {
            "usage": psutil.cpu_percent(interval=0.5),
            "cores": psutil.cpu_count()
        },

        "memory": {
            "total": memory.total,
            "used": memory.used,
            "available": memory.available,
            "percent": memory.percent
        },

        "disk": {
            "total": disk.total,
            "used": disk.used,
            "free": disk.free,
            "percent": disk.percent
        },

        "uptime": int(time.time() - psutil.boot_time())
    })


# =========================
# PROCESSES
# =========================

@app.route("/api/processes", methods=["GET"])
def processes():

    processes = []

    for process in psutil.process_iter(
        ["pid", "name", "username", "cpu_percent", "memory_percent"]
    ):
        try:

            info = process.info

            processes.append({
                "pid": info["pid"],
                "name": info["name"],
                "username": info["username"],
                "cpu": round(info["cpu_percent"], 2),
                "memory": round(info["memory_percent"], 2)
            })

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    processes.sort(
        key=lambda process: process["cpu"],
        reverse=True
    )

    return jsonify(processes[:20])


# =========================
# NETWORK
# =========================

@app.route("/api/network", methods=["GET"])
def network_info():

    network = psutil.net_io_counters()

    interfaces = {}

    for name, addresses in psutil.net_if_addrs().items():

        interfaces[name] = []

        for address in addresses:

            interfaces[name].append({
                "family": str(address.family),
                "address": address.address,
                "netmask": address.netmask
            })

    return jsonify({
        "bytes_sent": network.bytes_sent,
        "bytes_received": network.bytes_recv,
        "packets_sent": network.packets_sent,
        "packets_received": network.packets_recv,
        "interfaces": interfaces
    })


# =========================
# SERVICES
# =========================

@app.route("/api/services", methods=["GET"])
def services():

    services = []

    try:

        import subprocess

        result = subprocess.run(
            [
                "systemctl",
                "list-units",
                "--type=service",
                "--all",
                "--no-pager",
                "--no-legend"
            ],
            capture_output=True,
            text=True,
            timeout=10
        )

        for line in result.stdout.splitlines():

            parts = line.split(None, 4)

            if len(parts) >= 4:

                services.append({
                    "name": parts[0],
                    "load": parts[1],
                    "active": parts[2],
                    "sub": parts[3],
                    "description": parts[4] if len(parts) > 4 else ""
                })

    except Exception as error:

        return jsonify({
            "error": str(error)
        }), 500

    return jsonify(services)


# =========================
# DISK
# =========================

@app.route("/api/disk", methods=["GET"])
def disk_info():

    disks = []

    partitions = psutil.disk_partitions(
        all=False
    )

    for partition in partitions:

        try:

            usage = psutil.disk_usage(
                partition.mountpoint
            )

            disks.append({
                "device": partition.device,
                "mountpoint": partition.mountpoint,
                "filesystem": partition.fstype,
                "total": usage.total,
                "used": usage.used,
                "free": usage.free,
                "percent": usage.percent
            })

        except PermissionError:
            continue

    return jsonify(disks)


# =========================
# START SERVER
# =========================

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
