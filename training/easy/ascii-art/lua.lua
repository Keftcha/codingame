L = tonumber(io.read())
H = tonumber(io.read())
T = string.lower(io.read())

for i=0,H-1 do
    ROW = io.read()
    line = ""
    for letter in T:gmatch"." do
        if letter ~= "" then
            local idx = string.byte(letter)-97
            if (idx < 0) or (26 < idx) then
                idx = 26
            end
            line = line .. string.sub(ROW, (idx*L)+1, ((idx+1)*L))
        end
    end
    print(line)
end
