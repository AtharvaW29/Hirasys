import Image from 'next/image'
import { faBorderAll, faGear } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { SideBarNavDrawer } from './SideBarItems'

const dashboardItems = [
  { name: 'Messages', link: '/dashboard/messages' },
  { name: 'Tasks', link: '/dashboard/tasks' },
  {
    name: 'Inbox',
    link: '/dashboard/inbox',
  },
]

const processItems = [
  { name: 'Create new', link: '/process/create' },
  { name: 'Edit', link: '/process/edit' },
]

const SideBar = () => {
  return (
    <div className="h-screen w-[20%] sticky top-0 left-0 py-3 px-4 bg-overlay border-r-1 space-y-10">
      <Image
        src={'/images/mainLogo.png'}
        alt="Hirasys Logo"
        width={180}
        height={200}
      />
      <div className="space-y-3 ">
        <SideBarNavDrawer
          title="Dashboard"
          link="/dashboard"
          items={dashboardItems}
          icon={<FontAwesomeIcon icon={faBorderAll} className="h-4 w-4" />}
        />

        <SideBarNavDrawer
          title="Processes"
          link="/process"
          items={processItems}
          icon={<FontAwesomeIcon icon={faGear} className="h-4 w-4" />}
        />
      </div>
    </div>
  )
}

export default SideBar
