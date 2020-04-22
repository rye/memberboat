# The Membership Configuration Schema

A Membership Configuration specifies, for a given set of `orgs` and their corresponding `repos`, which of the `accounts` are allowed to access which resources, and with which permissions.

## The Configuration

A configuration file is assumed to be YAML or JSON; it must be deserializable and valid according to the parser.

### (required) `users`

The reserved and required top level key `users` is a _map_ containing keys that correspond to GitHub usernames and values that contain information.
There are no required keys or values for the values in the `users` map, but it is recommended to use this place to store information about a user's general characteristics.

#### Examples

```yaml
users:
  rye:
 	  # ...
  drewvolz:
    # ...
  dummy:
    # ...
```

### (required) `organizations`

The reserved and required top level key `organizations` is a _map_ containing keys that correspond to GitHub organization names, and values corresponding to specs for those.

#### Examples

```yaml
organizations:
  boat-sandbox:
    # ...
```
