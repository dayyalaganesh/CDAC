echo "Enter the number:"
read num
if [ $num -lt  0 ]
then
echo "negative number"
elif [ $num -gt 0 ]
then 
echo "positive number"
else
echo "zero"
fi

