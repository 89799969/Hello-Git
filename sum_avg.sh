#!/bin/bash

# 定义文件路径
input_file="numbers.txt"
output_file="result.json"

# 初始化变量
sum=0
count=0

# 读取文件中的每个数字
while read -r number; do
    if [[ "$number" =~ ^-?[0-9]+$ ]]; then  # 确保数字是有效的
        sum=$((sum + number))  # 计算总和
        count=$((count + 1))   # 统计数字个数
    else
        echo "警告: 文件中包含非数字内容 '$number'"
    fi
done < "$input_file"

# 计算平均值
if [ $count -ne 0 ]; then
    avg=$(echo "scale=2; $sum / $count" | bc)  # 使用 bc 计算精确的浮点数
else
    avg=0
fi

# 输出到 JSON 文件
echo "{\"sum\": $sum, \"average\": $avg}" > "$output_file"

# 显示结果
echo "总和: $sum, 平均值: $avg"
