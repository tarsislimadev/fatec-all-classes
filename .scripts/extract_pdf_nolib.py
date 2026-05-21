import sys, re, zlib

if len(sys.argv) < 2:
    print("Usage: python extract_pdf_nolib.py <pdf-path>")
    sys.exit(1)

path = sys.argv[1]
with open(path, 'rb') as f:
    data = f.read()

streams = []
start = 0
while True:
    idx = data.find(b'stream', start)
    if idx == -1:
        break
    s = idx + len(b'stream')
    # skip newline(s)
    if data[s:s+2] == b'\r\n':
        s += 2
    elif data[s:s+1] == b'\n':
        s += 1
    end = data.find(b'endstream', s)
    if end == -1:
        break
    stream_data = data[s:end]
    streams.append(stream_data)
    start = end + len(b'endstream')

extracted_texts = []
for i, stream in enumerate(streams, start=1):
    try:
        out = zlib.decompress(stream)
    except Exception:
        # not a compressed stream or decompression failed
        continue
    try:
        text = out.decode('latin-1')
    except Exception:
        text = out.decode('latin-1', errors='ignore')
    # extract literal strings in parentheses
    matches = re.findall(r'\(([^)]*)\)', text)
    if matches:
        for m in matches:
            m2 = m.replace('\\n','\n').replace('\\r','\r')
            extracted_texts.append(m2)

# Fallback: find ASCII runs in entire file
if not extracted_texts:
    ascii_runs = re.findall(rb'[\x20-\x7E]{4,}', data)
    for run in ascii_runs:
        try:
            extracted_texts.append(run.decode('latin-1'))
        except:
            pass

if not extracted_texts:
    print('(no extractable text found)')
else:
    for i, t in enumerate(extracted_texts, start=1):
        print(f'--- Text #{i} ---')
        print(t)
