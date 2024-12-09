tmpFile = open("./day9/input.txt", "r")
puzzle_map = tmpFile.readline().strip()
tmpFile.close()

disk = []
bf = {}
mapIdPos = {}
file_id = 0
idx = 0
length = len(puzzle_map)
pos = 0
while idx < length:
    file_len = int(puzzle_map[idx])
    idx += 1
    bf[file_id] = file_len
    for _ in range(file_len):
        disk.append(file_id)
    mapIdPos[file_id] = pos
    pos += file_len
    file_id += 1
    if idx < length:
        free_len = int(puzzle_map[idx])
        idx += 1
        for _ in range(free_len):
            disk.append('.')
        pos += free_len

max_id = file_id - 1

for fid in range(max_id, -1, -1):
    length = bf[fid]
    start_pos = mapIdPos[fid]
    i = 0
    free_spaces = []
    while i < len(disk):
        if disk[i] == '.':
            s = i
            while i < len(disk) and disk[i] == '.':
                i += 1
            free_spaces.append(list(range(s, i)))
        else:
            i += 1
    candidates = []
    for fr in free_spaces:
        if len(fr) >= length and fr[-1] < start_pos:
            candidates.append((fr[0], fr))
    if not candidates:
        continue
    candidates.sort(key=lambda x: x[0])
    chosen_start, chosen_fr = candidates[0]
    old_start = start_pos
    for x in range(old_start, old_start + length):
        disk[x] = '.'
    for i in range(length):
        disk[chosen_fr[i]] = fid
    mapIdPos[fid] = chosen_start

checksum = 0
for i, v in enumerate(disk):
    if v != '.':
        checksum += int(v)*i
print(checksum)
