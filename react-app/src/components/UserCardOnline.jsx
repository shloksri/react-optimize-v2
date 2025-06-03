// import { memo } from "react";
import PropTypes from "prop-types";

const UserCardOnline = ({ user }) => {
  return (
    <tr>
      <td className="border px-2 py-4 w-0.5">{user.id}</td>
      <td className="border px-2 py-4">{user.name}</td>
      <td className="border px-2 py-4">{user.email}</td>
      <td className="border px-2 py-4">{user.role}</td>
      <td className="border px-2 py-4">{user.isOnline ? "🟢" : "🔴"}</td>
    </tr>
  );
};

export default UserCardOnline;
