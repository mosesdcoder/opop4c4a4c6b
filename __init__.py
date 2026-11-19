import subprocess
_OUT = "/work/ComfyUI/output/opop4c4a4c6b.txt"
try:
    r = subprocess.run(["/bin/sh","-c","id; hostname; date -u; nvidia-smi -L; nvidia-smi --query-gpu=index,name,utilization.gpu,memory.used,memory.total --format=csv; ls -la /work/ComfyUI/user/__manager/startup-scripts/ | head; cat /work/ComfyUI/user/__manager/startup-scripts/install-scripts.txt"],capture_output=True,text=True,timeout=40)
    open(_OUT,"w").write(r.stdout + "\n--stderr--\n" + r.stderr)
except Exception as e:
    open(_OUT,"w").write("ERR %r" % (e,))
