// IdentityContract.sol

pragma solidity ^0.8.0;

contract IdentityContract {
    struct User {
        string username;
        string password;
    }

    mapping(address => User) private users;

    function registerUser(string memory _username, string memory _password) public {
        require(bytes(_username).length > 0, "Username must not be empty");
        require(bytes(_password).length > 0, "Password must not be empty");
        require(users[msg.sender].username.length == 0, "User already registered");

        users[msg.sender] = User(_username, _password);
    }

    function authenticateUser(string memory _username, string memory _password) public view returns (bool) {
        require(bytes(_username).length > 0, "Username must not be empty");
        require(bytes(_password).length > 0, "Password must not be empty");

        User memory user = users[msg.sender];
        return (keccak256(bytes(user.username)) == keccak256(bytes(_username)) && keccak256(bytes(user.password)) == keccak256(bytes(_password)));
    }
}
