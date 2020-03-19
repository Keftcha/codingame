b = gets.chomp.split "0"

maxOne = 1
for idx in 0..b.length-2 do
    maxOne = [maxOne, (b[idx].length + b[idx+1].length + 1)].max
end

puts maxOne
