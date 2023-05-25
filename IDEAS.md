# clean_atoms
Purpose is to rename atom names in the following scenario

There are two levels of names
- The residue name i.e. `ALA`
- The atom name i.e. `H3`

Replacements can take place potentially three selection methods
1. Match against the atom name alone
2. Match against the residue name alone
3. Match against a combination of the residue + atom name

Once a selection is made (for any of the above selections) then a replacement
can be made for
1. The atom name
2. The residue name
3. Both the atom and residue name

Some examples of the above scenarios

**Match atom names -> Replace atom names**
```python
if atom.name == 'H5\'':
    atom.name = 'H5\'1'
```

**Match atom names -> Replace residue names**
```python
if atom.name == 'OXT':
    residue.name = 'C'+residue.name
```

**Match atom names -> Replace atom and residue names**
```python
if atom.name in ('K+', 'K', 'K\+1', 'k', 'k+'):
    atom.name = 'K'
    residue.name = 'K'
```

**Match atom and residue names -> replace residue name**
```python
if residue.name in ('ALA', 'ARG'):
    for atom in residue.atoms:
        if atom.name == 'H3':
            residue.name = 'N'+residue.name
```

etc.

Perhaps a configurable way to describe this is
```json
{
    "replacements": [
        {
            "description": "replace ...",
            "selection": {
                "atoms": ["H5'", "H2'"],
            },
            "replacement": {
                "atom": "{atom_name}1"
            }
        },
        {
            "description": "replace ...",
            "selection": {
                "residues": ["ALA", "ARG", "ASN"],
                "atoms": ["H3"],
            },
            "replacement": {
                "residue": "N{residue_name}"
            }
        },
        {
            "description": "Normalize Chlorines",
            "selection": {
                "atoms": ["CL", "CL-", "CL1-"],
            },
            "replacement": {
                "residue": "CL",
                "atom": "CL"
            }
        }
    ]
}
```

```yaml
replacements:
    - description: "Normalize Chlorines"
      selection:
          atoms: ["H5'", "H2'"]
      replacement:
          atom: "{atom_name}1"
    - description: "Foo bar"
      selection:
          atoms: "H3"
      replacement:
          atom: "H3'"
```

# read_prm
This is nothing more than
```bash
grep "^atom" param_file > "atom_lines"
```
