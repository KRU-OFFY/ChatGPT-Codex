param(
    [string]$SkillPath = (Split-Path -Parent $PSScriptRoot)
)

$ErrorActionPreference = "Stop"
$SkillFile = Join-Path $SkillPath "SKILL.md"

if (-not (Test-Path $SkillFile)) {
    throw "Missing SKILL.md: $SkillFile"
}

$content = Get-Content -Raw -Path $SkillFile
if ($content -notmatch '(?ms)^---\s*\r?\n.*?^name:\s*doc-coauthoring\s*$.*?^description:\s*.+?^---\s*$') {
    throw "Invalid or incomplete YAML frontmatter in SKILL.md"
}

Write-Host "Validation passed: $SkillFile"
