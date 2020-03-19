n = gets.to_i
inputs = gets.split(" ")

pertes = 0
vmax = vmin = nil

for i in 0..(n-1)
    v = inputs[i].to_i
    if vmax == nil or vmax < v
        vmax = vmin = v
        next
    end
    if vmin <= v
        next
    end
    vmin = v
    pertes = [pertes, vmin - vmax].min
end

puts pertes
