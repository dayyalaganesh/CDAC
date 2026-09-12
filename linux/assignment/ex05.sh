echo "Enter the student marks:"
read marks
if [ $marks -ge 90 ] && [ $marks -le 100 ]
then 
echo "GRADE A "
elif [ $marks -ge 75 ] && [ $marks -le 89 ]
then 
echo "GRADE B"
elif [ $marks -ge 60 ] && [ $marks -le 74 ]
then
echo "GRADE C"
elif [ $marks -ge 50 ] && [ $marks -le 59 ]
then
echo "GRADE D"
elif [ $marks -ge 0 ] && [ $marks -le 49 ]
then
echo "FAIL"
else
echo "INVALID INPUT"
fi

