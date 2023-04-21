
$pyout = @(python "networking 3.py")
for ( $i = 0 ; $i -lt 3; $i++) {
	$pyout = @(Write-Output $pyout[0].remove(0,8) | python "Networking 3.py") ;
	$pyout
}