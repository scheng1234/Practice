function race($v1, $v2, $g)
{
    # v1 is A's speed (ft/hr)
    # v2 is B's speed (ft/hr)
    # $g is A's lead in ft on B
    $x = $g/($v2 - $v1)
    if ($v2 -lt $v1){$null}
    else{$data = ([int][math]::Floor($x), [int][math]::Floor($x*60 % 60), [int][math]::Floor($x*3600 % 60))}
    $data -join " "
}