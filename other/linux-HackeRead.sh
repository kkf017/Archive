
read x
echo $x

#######################################

read x
read y
echo $(expr $x + $y)
echo $(($x * $y))

#####################################
read x
read y

if [ "$x" -gt "$y" ] ; then
    echo "X is greater than Y"
        
elif [ "$x" -eq "$y" ]; then 
    echo "X is equal to Y"
        
else
    echo "X is less than Y"

fi

###################################
read var

if [ $var = "Y" -o $var = "y" ]
then
    echo "YES"
else
    echo "NO"
fi

#####################################
