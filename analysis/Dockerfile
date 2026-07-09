FROM ubuntu:22.04

# Set non-interactive mode for apt
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=UTC

# Install analysis tools
RUN apt-get update && apt-get install -y \
    file \
    binutils \
    xxd \
    bsdmainutils \
    binwalk \
    exiftool \
    clamav \
    yara \
    upx \
    && rm -rf /var/lib/apt/lists/*

# Create analysis directory
WORKDIR /malware_analysis
COPY core_fix_v2.exe /malware_analysis/

# Create a simple analysis script
RUN echo '#!/bin/bash\n\
echo "=== File Information ==="\n\
file core_fix_v2.exe\n\
echo -e "\n=== File Size ==="\n\
ls -lh core_fix_v2.exe\n\
echo -e "\n=== Strings Analysis (first 50 lines) ==="\n\
strings core_fix_v2.exe | head -50\n\
echo -e "\n=== PE Header Information ==="\n\
objdump -x core_fix_v2.exe | head -30\n\
echo -e "\n=== Sections ==="\n\
objdump -h core_fix_v2.exe\n\
echo -e "\n=== Imports ==="\n\
objdump -p core_fix_v2.exe | grep -A 20 "DLL Name"\n\
echo -e "\n=== YARA Scan ==="\n\
yara -r /etc/yara-rules/ core_fix_v2.exe 2>/dev/null || echo "No YARA rules configured"\n\
echo -e "\n=== ClamAV Scan ==="\n\
clamscan --no-summary core_fix_v2.exe\n\
' > analyze.sh && chmod +x analyze.sh

ENTRYPOINT ["/bin/bash", "/malware_analysis/analyze.sh"]
