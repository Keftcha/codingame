n = gets.to_i

conv = Hash.new
n.times do
    b, c = gets.split(" ")
    conv[b] = c.to_i
end
s = gets.chomp

word = ""
pb, pr = 0, 1
while pr <= s.length do
    conv.each do |key, value|
        if key == s.slice(pb..pr-1) then
            word += value.chr
            pb = pr
        end
    end
    pr += 1
end

if pr - pb > 1 then
    puts("DECODE FAIL AT INDEX " + pb.to_s)
else
    puts word
end
