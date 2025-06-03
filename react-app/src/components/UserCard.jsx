import PropTypes from "prop-types";
import { memo } from "react";

const UserCard = ({ user }) => {
  return (
    <tr>
      <td className="border px-2 py-4 w-0.5">{user.id}</td>
      <td className="border px-2 py-4">{user.name}</td>
      <td className="border px-2 py-4">{user.email}</td>
      <td className="border px-2 py-4">{user.role}</td>
    </tr>
  );
};

UserCard.propTypes = {
  user: PropTypes.shape({
    id: PropTypes.number,
    name: PropTypes.string,
    phone: PropTypes.string,
    email: PropTypes.string,
    role: PropTypes.string,
    department: PropTypes.string,
    permissions: PropTypes.string,
    lastLogin: PropTypes.string,
    isOnline: PropTypes.bool,
  }).isRequired,
};

export default UserCard;
