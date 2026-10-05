# Topic profile template

Create one profile per VTR type.

```yaml
profile_name: ""
purpose: ""
audience: ""
hard_duration_seconds: 300
target_duration_seconds: 285
authoritative_sources: []
required_sections: []
scored_criteria: []
required_evidence: []
prohibited_claims: []
privacy_rules: []
brand_assets: []
narration_tone: "formal"
visual_style: "evidence-led"
output:
  width: 1920
  height: 1080
  fps: 30
  video_codec: "h264"
  audio_codec: "aac"
acceptance_checks: []
```

## Adaptation procedure

1. Copy the production core without changing tested editing behavior.
2. Replace the purpose, audience, rubric, narrative sections, evidence rules, terminology, and duration.
3. Add only topic-specific references and assets.
4. Test the new profile with representative inputs.
5. Confirm that the generated Skill triggers on real user phrases for that topic.
