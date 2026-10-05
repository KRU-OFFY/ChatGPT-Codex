param(
    [string]$DestinationRoot = "$HOME\.agents\skills"
)

$ErrorActionPreference = "Stop"
$SkillRoot = Split-Path -Parent $PSScriptRoot
$SkillName = "doc-coauthoring"
$Destination = Join-Path $DestinationRoot $SkillName

New-Item -ItemType Directory -Force -Path $Destination | Out-Null
Copy-Item -Path (Join-Path $SkillRoot "*") -Destination $Destination -Recurse -Force

Write-Host "Installed skill: $Destination"
Write-Host "SKILL.md: $(Join-Path $Destination 'SKILL.md')"
