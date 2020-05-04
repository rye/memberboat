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
An organization has a few reserved keys.

#### (required) `members`

The `members` key contains an array of `username: role` combinations, where `role` is either `admin` or `member`.

**Please note:** This key configures the membership of the _organization_.
Team membership is not available for configuration yet, but will be handled differently.
To convert a user to an external collaborator, you must do that manually.

#### Examples

```yaml
organizations:
  boat-sandbox:
    members:
    - rye: admin
    - drewvolz: admin
    - dummy: member
```

#### Example with Selections based on User attributes

```yaml
users:
  rye:
    type: student
    year: 2020
  drewvolz:
    type: alumnus
    year: 2016
  dummy:
    type: external

organizations:
  boat-sandbox:
    members:
      # This rule matches all users where the type is alumnus and applies the "admin" role to those users.
      - users:
          where: { type: alumnus }
          role: admin
      - dummy: member
```
