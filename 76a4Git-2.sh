#!/bin/bash
# http://www.qlcoder.com/task/76a4
# 执行此代码可以找到第一个可用的commit。

pwd
until python unit.py; do
	git reset --hard HEAD~1
done
echo FIND!

