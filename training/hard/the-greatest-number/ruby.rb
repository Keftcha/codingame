n = gets.to_i
input = gets.chomp.split(" ").sort()

if input.include? "-"
    if input.include? "."
        input[1], input[2] = input[2], input[1]
    end
else
    input.reverse!
    if input.include? "."
        input[-2], input[-1] = input[-1], input[-2]
        if input[-1] == "0"
            input.delete_at -1
            input.delete_at -1
        end
    end
end

input = input.join ""
puts input.to_f != 0 ? input : 0
