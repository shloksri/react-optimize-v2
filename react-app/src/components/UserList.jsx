// src/components/UserList.jsx
import { useEffect, useState } from "react";
import UserCard from "./UserCard";
import usersData from "../data/mockUsers.json";
import UserCardOnline from "./UserCardOnline";

const UserList = () => {
  const [users, setUsers] = useState(usersData);

  useEffect(() => {
    const interval = setInterval(() => {
      setUsers((prevUsers) =>
        prevUsers.map((user) => {
          if (user.id === 2 || user.id === 3) {
            return {
              ...user,
              isOnline: !user.isOnline, // Toggle status
            };
          }
          return user; // Leave other users untouched
        })
      );
    }, 2000);

    return () => clearInterval(interval);
  }, []);

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-50">
      <div className="p-6 bg-white rounded shadow-md">
        <h2 className="text-xl font-bold mb-4 text-center">Team Members</h2>
        <table className="table-auto border-collapse bg-white shadow-md">
          <thead>
            <tr className="bg-gray-100">
              <th className="border px-4 py-2">ID</th>
              <th className="border px-4 py-2">Name</th>
              <th className="border px-4 py-2">Email</th>
              <th className="border px-4 py-2">Role</th>
              {/* <th className="border px-4 py-2">Online Status</th> */}
            </tr>
          </thead>
          <tbody>
            {users.map((user) => (
              <UserCard key={user.id} user={user} />
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default UserList;
